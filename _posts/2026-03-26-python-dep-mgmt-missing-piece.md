---
title: "Python Dependency Management is Missing a Piece"
date: 2026-03-26 20:38:00 -0600
---

*A comparison of dependency resolution across software ecosystems, and why Python's model leaves library authors with no good options.*

---

## The Core Problem

I am increasingly convinced that Python's dependency management ecosystem is fundamentally broken compared to Java's, for one reason: Python's package metadata has a structural gap that forces library authors into an impossible choice between **reproducibility** and **composability**.

Here's the argument in brief: in Java, [Maven](https://maven.apache.org/)'s `pom.xml` provides *soft* version pinning: library authors declare "I verified dependency libfoo works at version 2.28.0—use it as a starting point, but feel free to move if something else in the mix requires otherwise." Python's `pyproject.toml` offers no equivalent: you can express a constraint (`>=2.28.0,<3`), but you cannot communicate "this is a version I verified works." Lockfiles provide strict reproducibility, but at the cost of composability—they are only a partial solution for communicating a signal missing from primary project metadata.

---

## Dependency Management Approaches

### How Java Dependencies Work

When a Maven POM declares:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.12.0</version>
</dependency>
```

that version is not a hard pin. It's a *preference*: a soft signal to the resolver saying "the author verified this works; use it unless something else in the dependency tree says otherwise." Downstream projects can override it, but this verified baseline is embedded in the published artifact and available to any consumer, forever. When combined with a reproducible dependency resolution strategy, the POM is effectively a lockfile: a fresh build from a specific POM version is reproducible by default thanks to [Maven's "nearest wins" dependency mediation rule](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html).

This design works in practice because the Java language and ecosystem has a strong history and culture of backward compatibility and stable ABIs. A library compiled against Java 8 usually runs on Java 21 unchanged, reducing the need for new library releases for the sole purpose of supporting newer runtime versions.

### How Python Dependencies Work

Python's dependency resolution—whether via `pip`, `uv`, or `conda`—recognizes only hard constraints: ranges, exact pins, and exclusions. [PEP 508](https://peps.python.org/pep-0508/) offers no concept of a preference or soft pin.

This forces library authors into a dilemma:

- **Exact pin** (`requests==2.28.0`): Reproducible, but breaks composability. If library A pins `requests==2.28.0` and library B pins `requests==2.29.0`, they cannot coexist. Resolution fails.
- **Range** (`requests>=2,<3`): Composable, but loses any version anchor entirely. Consumers have no reference point for a configuration the author verified works. A new `2.x` release of `requests` upstream breaks reproducibility, potentially introducing security issues or bugs.

The lockfile (e.g. `uv.lock` or `poetry.lock`) recovers reproducibility—but only for applications. Most libraries don't publish lockfiles alongside releases on PyPI, so consumers of library releases are silently subject to transitive churn with every fresh install. No verified baseline exists in the published artifact.

It is worth noting here that this design flaw is not limited to Python—there are many dependency management ecosystems with exactly the same problem: JavaScript's `package.json`, Rust's `Cargo.toml`, Conda's `environment.yml` (though see [Bills of Materials and Ecosystem Coordination](#bills-of-materials-and-ecosystem-coordination) below), PHP's `composer.json`, Ruby's `Gemfile`, Swift's `Package.swift`, and Lua's `rockspec`, to name a few.

### Aside: How Go Dependencies Work

Like Java/Maven, [Go](https://go.dev/) mediates dependencies in a reproducible way. Its [Minimum Version Selection](https://go.dev/ref/mod#minimal-version-selection) (MVS) approach works as follows:

- `go.mod` declares the *minimum* version of each dependency the module requires.
- The resolver selects the highest minimum across all transitive dependencies—the simplest version that satisfies everyone.

Like Maven, the algorithm is deterministic without a lockfile, composable by construction, and embeds a version anchor: the minimum version known to work. Unlike Maven, however, MVS avoids situational version downgrades in complex dependency trees, while still providing the metadata-level version anchor that Python lacks entirely.

The [.NET/NuGet `PackageReference`](https://github.com/NuGet/docs.microsoft.com-nuget/blob/abda464685aeab8292e883702ba1d0229b920e0b/docs/consume-packages/Package-References-in-Project-Files.md) mechanism works in a similar fashion to Go, with soft version declarations from which the highest minimum is selected when composing dependencies.

### Cross-Ecosystem Comparison

The table below examines each ecosystem's dependency artifacts along several dimensions:

* **Reproducible** – Does this artifact alone guarantee an identical dependency set on every install?
* **Composable** – Can a downstream resolver incorporate this into a combined dependency tree?
* **Version anchor** – Does this artifact communicate a known-good reference version, as a non-binding signal to downstream resolvers?
* **Constraint expressiveness** – How flexible are version specifications?
* **Resolution algorithm** – What strategy does the resolver use?
* **Cross-platform** – Is the artifact platform-independent?
* **Published with library releases** – Is this artifact routinely published alongside library releases?

| Ecosystem | Artifact | Reproducible | Composable | Version anchor | Constraint expressiveness | Resolution algorithm | Cross-platform | Published with library releases |
|---|---|---|---|---|---|---|---|---|
| Maven | `pom.xml` | Yes | Yes | **Yes** (soft preference, nearest-wins) | Ranges, exact, exclusions | Nearest-wins | Mostly | Always |
| Gradle | `build.gradle` | No | Yes | No | Ranges, exact, exclusions, arbitrary logic | Varies | Mostly | Usually |
| Gradle | Declarative Gradle | Not yet\* | Yes | No | Ranges, exact | Varies | Mostly | Rarely |
| Python | `pyproject.toml` | No | Yes | **No** | Ranges, exact, exclusions—very flexible | SAT/backtracking | No | Always |
| Python | `requirements.txt` | Depends | No | No | Ranges or exact (ambiguous by design) | None / SAT | No | Rarely |
| Python | `uv.lock` / `poetry.lock` | Yes | No | Yes (but moot—not composable) | Exact (lockfile) | None (pre-resolved) | Yes | **Never** |
| Conda | `environment.yml` | No | Yes | **No** | Ranges, exact | SAT/backtracking | No | Always |
| Conda | `conda-lock.yml` | Yes | No | Yes (but moot) | Exact (lockfile) | None (pre-resolved) | Yes | **Never** |
| Pixi | `pixi.lock` | Yes | No | Yes (but moot) | Exact (lockfile) | None (pre-resolved) | Yes | **Never** |
| conda-forge | pinnings‡ | Yes | Partial | Yes (within conda-forge) | Exact, centrally managed | N/A (build system) | Yes | Always (within build system) |
| R | `DESCRIPTION` | No | Yes | No† | Ranges, exact | SAT/backtracking | Mostly | Always |
| R | `renv.lock` / `packrat.lock` | Yes | No | Yes (but moot) | Exact (lockfile) | None (pre-resolved) | Mostly | **Never** |
| npm | `package.json` | No | Yes | No | Ranges, exact, semver operators | SAT/backtracking | Mostly | Always |
| npm | `package-lock.json` | Yes | No | Yes (but moot) | Exact (lockfile) | None | Mostly | Never |
| Rust | `Cargo.toml` | No | Yes | No | Ranges, exact | SAT/backtracking | Yes | Always |
| Rust | `Cargo.lock` | Yes | No | Yes (but moot) | Exact (lockfile) | None | Yes | Never (for libraries) |
| Go | `go.mod` | Yes | Yes | **Yes** (minimum, raiseable by MVS) | Minimum version | MVS | Yes | Always |
| Go | `go.sum` | Yes | No | Yes (but moot) | Exact hash (integrity) | None | Yes | Always |
| .NET | `*.csproj` (PackageReference) | Mostly | Yes | **Yes** (minimum, lowest-applicable) | Ranges, exact, floating | Lowest-applicable | Mostly | Always |
| .NET | `packages.lock.json` | Yes | No | Yes (but moot) | Exact (lockfile) | None (pre-resolved) | Mostly | Never |
| Lua | `rockspec` | No | Yes | No | Basic ranges, exact | SAT/backtracking | Mostly | Always |

<div style="font-size: 0.75em; margin-top: -1em" markdown=1>

\* Declarative Gradle is not yet stable.  
† CRAN runs ecosystem-wide reverse-dependency checks against all packages on the registry, acting as a partial BOM validator: packages that break their dependents are delisted.  
‡ conda-forge pinnings (`conda-forge-pinning`) are the closest Python-ecosystem analog to a Maven BOM: a centrally curated set of pinned versions for key compiled dependencies against which all conda-forge packages are built and tested. Usable only within the conda-forge build system, not by arbitrary downstream projects.

</div>

The story the table tells is stark. `pom.xml`, `go.mod`, and .NET's `PackageReference` are the only artifacts that simultaneously score well on reproducibility, composability, version anchor, and "published always." Python's `pyproject.toml` and Conda's `environment.yml` are composable and expressively flexible but have no version anchor. Their respective lockfiles are reproducible but are never published alongside library releases and are not composable. The gap between them is exactly the missing mechanism.

The conda-forge pinnings row is intentionally different in kind from the others—it is an ecosystem coordinator rather than a per-project artifact, which is why it appears in the BOM discussion below. It is the only entry in the Python/Conda world that provides any version anchor at the ecosystem level.

### Bills of Materials and Ecosystem Coordination

Maven's story doesn't stop at individual POMs. Large Java ecosystems often use a second tier of dependency management known as a *Bill of Materials* (BOM): a special POM that declares `<dependencyManagement>` entries for an entire suite of components, asserting that these specific versions are known to work together. Any project that imports the BOM via `<scope>import</scope>...` within `<dependencyManagement>` gets consistent transitive dependency resolution across the whole suite.

But a BOM only makes a *claim* of compatibility. The harder question is whether that claim holds. The [SciJava BOM](https://github.com/scijava/pom-scijava) employs a [comprehensive testing process](https://github.com/scijava/bombast), run as a continuous integration (CI) workflow that rebuilds each BOM-managed component pinned to the managed versions—including all unit tests—verifying that the suite is internally consistent at compile time and runtime. The BOM is the contract; the passing CI workflow is the evidence.

Together, all of this forms a robust three-tier dependency management infrastructure:

1. **Reproducible and composable dependencies** with soft version pins providing a known-good reference baseline (`pom.xml`, `go.mod`; absent in `pyproject.toml`)
2. **Bills of Materials** to curate known-good version sets across components (Maven BOM; absent in PyPI)
3. **Soundness verification** testing to prove that curator's claims hold (SciJava bombast library; absent most everywhere else as a standard practice)

The closest Python analog to such an infrastructure is conda-forge's global pinnings (`conda-forge-pinning`), which maintains pinned versions for key compiled dependencies and builds all conda-forge packages against them. This is BOM-like and includes partial runtime compatibility validation. But it only works within Conda (not PyPI), and it focuses primarily on ABI compatibility of compiled extensions rather than full semantic compatibility. Beyond that, the Scientific Python community has [SPEC 0](https://scientific-python.org/specs/spec-0000/) and [other SPEC documents](https://scientific-python.org/specs/) that coordinate support windows across numpy, scipy, matplotlib, etc.—but these are human-level documentation, not machine-readable artifacts that any resolver can consume.

The table above suggests a third row category beyond *manifest* and *lockfile*: **ecosystem coordinator**. Only Maven BOMs and conda-forge pinnings have meaningful entries there.

---

## The ABI Dimension: Wheel Hell

Even if Python solved its metadata and soft-pinning problems, there is a second failure mode: the ABI matrix.

CPython's C ABI is intentionally unstable across minor versions. A compiled extension for Python 3.9 is a physically different binary from one for 3.10. This is by design—it lets C extensions access CPython internals for performance—but the practical consequence is that Python libraries backed by native code must maintain separate binary builds for every combination of (Python minor version) × (OS/platform). Free-threaded Python (3.13+) adds yet another axis to this matrix.

The result is a sort of *geologic strata*: time-layered bands on PyPI and conda-forge corresponding to Python version support windows. When composing five dependencies to meet some need, they may not all fall within a single band—perhaps one has dropped Python 3.11 support while another hasn't added Python 3.13 builds yet. Finding the intersection becomes a constraint satisfaction problem with a hard, non-negotiable runtime constraint.

[PEP 384](https://peps.python.org/pep-0508/) (the "stable ABI," `abi3` wheel tag) lets packages opt into a restricted API surface that is stable across Python versions, but adoption is not always possible because it requires giving up access to CPython internals that performance-critical packages like NumPy depend on.

The Python community has addressed the support-window dimension within scientific Python via [SPEC 0](https://scientific-python.org/specs/spec-0000/), which recommends dropping Python versions 3 years after their release and core dependencies 2 years after their release, coordinated across major packages. But SPEC 0 is only a recommendation, adoption is uneven, and it produces no machine-readable artifact that resolvers can consume. Each package's maintainers independently decide when to drop old Python versions, and the ecosystem ends up with packages at incompatible lifecycle stages.

The closest analog in another ecosystem is Rust's [Minimum Supported Rust Version](https://github.com/rust-lang/rfcs/blob/master/text/2495-min-rust-version.md) (MSRV) problem: library authors independently decide what minimum Rust compiler version they support, creating similar misalignment when composing crates. Rust has been [actively debating MSRV policies](https://github.com/rust-lang/rfcs/blob/master/text/3537-msrv-resolver.md), and `Cargo.toml` now has an [explicit `rust-version` field](https://doc.rust-lang.org/cargo/reference/rust-version.html) to make this machine-readable. Python's `requires-python` encodes only a minimum, not an intentional support window.

## Workarounds, Not Solutions

The Python ecosystem has produced several tools that partially address the missing version anchor. Each is a genuine improvement over nothing—but each is ultimately a workaround for a gap that should be closed at the metadata level.

### `uv --exclude-newer` and pixi's `exclude-newer`

Both `uv` and `pixi` offer a date-based resolution flag: `uv pip install --exclude-newer <date>`, and `exclude-newer = "YYYY-MM-DD"` in `pixi.toml`. The idea is that by ignoring packages published after a library's release date, you can reconstruct what was available when the author was testing.

This is much better than nothing—but it is guesswork, not a record:

- **The date is imprecise.** CI testing might run days or weeks before a release. The latest packages available at release time could be newer than those actually used in the test run.
- **It's an approximation, not fact.** The library author never captured their test environment. The resolver re-derives something plausible—but it may differ from what the author actually ran against.
- **A bad release before the cutoff is still included.** The date filter excludes packages released after the cutoff, but says nothing about the quality of releases before it.
- **It requires user initiative.** Nothing in the library's PyPI metadata tells downstream consumers to use `--exclude-newer`, or with what date.
- **Pixi has an additional structural limitation:** its `exclude-newer` [requires the `upload-time` field](https://pixi.prefix.dev/dev/reference/pixi_manifest/#exclude-newer-optional) specified in [PEP 700](https://peps.python.org/pep-0700/); packages lacking that field become unavailable entirely under the constraint.

### pip's `--constraint`

pip's [`--constraint` flag](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-c) lets you supply a file of version pins that act as bounds on resolution: unlike `--requirement`, constraints don't add packages to the install set—they only restrict what versions the resolver may choose among already-requested packages.

This is conceptually much stronger than `--exclude-newer`: instead of guessing by date, a library author can publish a known-good reference configuration as a constraint file. A user who wants reproducibility passes that file to pip.

A pip constraint file is, in this sense, exactly a BOM—it is the closest Python comes to what Maven's `<dependencyManagement>` import provides, serving as a curated, per-release list of known-good versions for a dependency suite. The crucial difference is that in Maven, importing a BOM is a first-class operation that the resolver performs automatically. With pip's `--constraints`, the user must manually locate and supply the file; nothing in the library's PyPI metadata points to it.

The limitations:
- **No discovery.** PyPI has no field for "here is the constraint file for this release." Users must already know it exists and where to find it.
- **Out-of-band publication.** Constraint files are typically hosted on GitHub or a project website—entirely outside the standard packaging machinery.
- **No automatic resolver integration.** The constraint file does not participate in dependency mediation on its own.
- **Limited tool support.** `pip` and `uv` support `--constraint` (uv also via the `UV_CONSTRAINT` environment variable), but `pixi` and `conda` do not offer an equivalent mechanism. More importantly, nothing in PyPI metadata points any tool to the right constraint file for a given release—support for the flag is moot without a standard way to discover the file.
- **Not composable.** If you depend on two libraries that each publish constraint files, there is no standard mechanism to merge them into a consistent resolution (although in many cases it might be doable to apply something like minimum version selection across multiple overlapping constraint files).

### Apache Airflow and napari: Proofs of Concept

There are some projects that publish constraints files as known-good baselines. For example, the [Apache Airflow](https://airflow.apache.org/) project, for each release, generates and publishes a pinned constraint file for every supported Python version, hosted as raw files in [orphan Git branches on GitHub](https://github.com/apache/airflow/branches/all?query=constraints) (e.g. `constraints-3.1.8`). Installation looks like:

```bash
pip install "apache-airflow[celery]==3.1.8" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.8/constraints-3.10.txt"
```

The Airflow maintainers [have reported](https://discuss.python.org/t/pre-pep-add-ability-to-install-a-package-with-reproducible-dependencies/99497/23) it has saved them from transitive breakage on numerous occasions. The [napari](https://napari.org/) project uses a similar approach, [publishing its constraint files](https://github.com/napari/napari/tree/v0.7.0/resources/constraints) on each branch under `resources/constraints` and [using them in CI workflows](https://github.com/napari/napari/blob/50df933a59a6cac83f36ef471a9809196f7e7a8d/.github/workflows/reusable_run_tox_test.yml#L57).

Both projects recognized the need to fill this dependency management gap, but had to implement their own ad hoc solutions, due to the lack of packaging standard for this purpose. As such, these constraint files are a **tier 1 workaround**: they publish known-good baseline configurations for each project's own dependency graph at release time, but with extra overhead and without discoverability. The labor involved is almost entirely infrastructure overhead: orphan branches, URL conventions, per-(version × Python) generation scripts, user documentation—all to communicate a signal that should be automatic with every component release.

This is categorically different from the **tier 2** work of curating a multi-project BOM and the **tier 3** work of verifying its claims. The [SciJava BOM](https://github.com/scijava/pom-scijava), for example, coordinates compatibility guarantees across hundreds of independent components spanning many different teams and release schedules. That curation labor is inherent to the coordination task—the hard part is not *recording* what was tested but *deciding* which versions of independent projects should be declared mutually compatible and then *verifying* that claim. Closing the tier 1 gap for all published components would nonetheless reduce the BOM maintenance burden, by providing better starting points leading to fewer surprises during BOM validation testing.

Airflow and napari demonstrate that demand for tier 1 exists and the approach works. But the absence of a standard is visible in the divergence between them: Airflow hosts constraint files in orphan Git branches; napari keeps them on each branch under `resources/constraints`. Both choices work, but neither is discoverable from PyPI, and each requires users to learn a project-specific convention. Absent a standard to converge on, most maintainers don't know this is something they should do at all, and those who do build their own solutions build them incompatibly. The result is a near-total absence of the practice across the ecosystem, with downstream consumers left to feel the pain of irreproducibility by default.

## The Standard Python Needs

What Python needs is a standard mechanism for library authors to publish "here is a baseline configuration known to work at the time of this release," as an automatic part of the package metadata. Such a baseline is not a claim that these are the *only* versions tested—most projects run a matrix of configurations, and a single lockfile cannot enumerate them all. Rather, it is a reference point: one verified configuration that a resolver can use as a soft preference signal, not a hard constraint, recovering most of Maven's reproducibility benefits while preserving composability. It would also open the door to Go-style Minimum Version Selection as a viable resolution strategy for Python.

This is not a fundamentally new idea—it's what Java, Go and .NET already provide, expressed differently. It just hasn't been built for Python. While the gap is technical, it has led to a corresponding cultural failure: loose ranges everywhere and lockfiles only for apps. The best way to turn the ship around is to close not only the technical gap, but also the cultural one by including this vital dependency version metadata automatically by default with every new PyPI release henceforth.

Encouragingly, there is an [ongoing Pre-PEP discussion](https://discuss.python.org/t/pre-pep-add-ability-to-install-a-package-with-reproducible-dependencies/99497) attempting to achieve exactly this goal by bundling a [PEP 751](https://peps.python.org/pep-0751/) `pylock.toml` file at `*.dist-info/pylock/` inside each wheel so tested dependencies travel with the release. Unfortunately, there is a core philosophical disagreement blocking this pre-PEP: [some maintainers argue](https://discuss.python.org/t/pre-pep-add-ability-to-install-a-package-with-reproducible-dependencies/99497/4) that wheels should remain pure library distributions, and that reproducibility is an application-layer concern, instead suggesting a parallel central lockfile index.

For closing Python's gap in dependency management, either way (internal or external to wheels) would work—but as of this writing, there is no consensus and thus no solution yet. And until the gap is closed, Python library consumers will continue to suffer from [transitive dependency churn](https://sethmlarson.dev/deprecations-via-warnings-dont-work-for-python-libraries), [irreproducible behavior over time](https://craftofcoding.wordpress.com/2017/01/27/pythons-achilles-heel/), brutal [supply chain attacks](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/), and [broken environments](https://xkcd.com/1987/).

---

*The author maintains the SciJava Bill of Materials and associated CI infrastructure. Opinions are informed by years of debugging transitive dependency failures with the Java and Python ecosystems.*
