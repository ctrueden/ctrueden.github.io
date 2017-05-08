#!/bin/sh
sed -i '' -E -e 's/\[([^]|]*)\|([^]]*)\]/[\2](\1)/g' $@
sed -i '' -E -e 's/\(\(([^|)]*)\|([^)]*)\)\)/[\2](\1)/g' $@
sed -i '' -E -e 's/\(\(([^|)]*)\)\)/[\1](\1)/g' $@
sed -i '' -E -e 's/^!+-? *$//g' $@
sed -i '' -E -e 's/^!!!!!!!-?(.*)/####### \1/g' $@
sed -i '' -E -e 's/^!!!!!!-?(.*)/###### \1/g' $@
sed -i '' -E -e 's/^!!!!!-?(.*)/##### \1/g' $@
sed -i '' -E -e 's/^!!!!-?(.*)/#### \1/g' $@
sed -i '' -E -e 's/^!!!-?(.*)/### \1/g' $@
sed -i '' -E -e 's/^!!-?(.*)/## \1/g' $@
sed -i '' -E -e 's/^!-?(.*)/# \1/g' $@
for f in $@
do
  perl -0777 -i -pe "s/^ *-=([^\n=]*)=-\n*/---\nlayout: page\ntitle: \1\npermalink: \/deus\/$f\ncategory: deus\n---\n/igs" "$f"
  perl -0777 -i -pe "s/^([^-])/---\nlayout: page\ntitle: $f\npermalink: \/deus\/$f\ncategory: deus\n---\n\1/igs" "$f"
  sed -i '' -E -e 's/-==(.*)==-/## \1/g' "$f"
  sed -i '' -E -e 's/-=(.*)=-/# \1/g' "$f"
done
