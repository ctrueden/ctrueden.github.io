---
layout: page
title: Sphere point calculator
permalink: /mystic/points/calculator/
category: mystic2
---
For convenience, here is a calculator for computing the number of points
a mystic receives at each level, as well as verifying the number of
building points required for a given point allocation.

<script>// <![CDATA[
function compute (form) {
  if (form.half.checked == true) half(form);
  else normal(form);
  left = parseInt(form.total.value);
  s1=parseInt(form.s1.value); left-=(s1+1)*s1/2;
  s2=parseInt(form.s2.value); left-=(s2+1)*s2/2;
  s3=parseInt(form.s3.value); left-=(s3+1)*s3/2;
  s4=parseInt(form.s4.value); left-=(s4+1)*s4/2;
  s5=parseInt(form.s5.value); left-=(s5+1)*s5/2;
  s6=parseInt(form.s6.value); left-=(s6+1)*s6/2;
  s7=parseInt(form.s7.value); left-=(s7+1)*s7/2;
  s8=parseInt(form.s8.value); left-=(s8+1)*s8/2;
  s9=parseInt(form.s9.value); left-=(s9+1)*s9/2;
  s10=parseInt(form.s10.value); left-=(s10+1)*s10/2;
  s11=parseInt(form.s11.value); left-=(s11+1)*s11/2;
  res=parseInt(form.res.value); left-=res;
  form.left.value = left;
}
function normal (form) {
  level = parseInt(form.level.value);
  key = parseInt(form.key.value);
  if (level < 1 || key < 0) {
    form.gain.value = "N/A";
    form.total.value = "N/A";
  }
  else {
    form.gain.value = 2*level+key;
    form.total.value = level*(level+key+1);
  }
}
function half (form) {
  level = parseInt(form.level.value);
  key = parseInt(form.key.value);
  if (level < 1 || key < 0) {
    form.gain.value = "N/A";
    form.total.value = "N/A";
  }
  else {
    if (key % 2 == 1) key--;
    form.gain.value = level+key/2;
    form.total.value = level*(level+1)/2 + level*(key/2);
  }
}
// ]]></script>
<form>
<table>
<tbody>
<tr>
<td>Level</td>
<td><input name="level" size="3" type="text" value="1" /></td>
<td>Ability modifier</td>
<td><input name="key" size="3" type="text" value="4" /></td>
<td>Half rate</td>
<td><input name="half" type="checkbox" /></td>
</tr>
<tr>
<td>Gain</td>
<td><input name="gain" readonly="readonly" size="3" type="text" value="6" /></td>
<td>Total</td>
<td><input name="total" readonly="readonly" size="3" type="text" value="6" /></td>
<td>Remain</td>
<td><input name="left" readonly="readonly" size="3" type="text" value="6" /></td>
</tr>
<tr>
<td>Creation</td>
<td><input name="s1" size="3" type="text" value="0" /></td>
<td>Destruction</td>
<td><input name="s2" size="3" type="text" value="0" /></td>
<td>Displacement</td>
<td><input name="s3" size="3" type="text" value="0" /></td>
</tr>
<tr>
<td>Divination</td>
<td><input name="s4" size="3" type="text" value="0" /></td>
<td>Enhancement</td>
<td><input name="s5" size="3" type="text" value="0" /></td>
<td>Healing</td>
<td><input name="s6" size="3" type="text" value="0" /></td>
</tr>
<tr>
<td>Illusion</td>
<td><input name="s7" size="3" type="text" value="0" /></td>
<td>Kinetics</td>
<td><input name="s8" size="3" type="text" value="0" /></td>
<td>Mind Control</td>
<td><input name="s9" size="3" type="text" value="0" /></td>
</tr>
<tr>
<td>Pyrotechnics</td>
<td><input name="s10" size="3" type="text" value="0" /></td>
<td>Transmutation</td>
<td><input name="s11" size="3" type="text" value="0" /></td>
<td>Reserve</td>
<td><input name="res" size="3" type="text" value="0" /></td>
</tr>
</tbody>
</table>
<p><input onclick="compute(this.form)" type="button" value="Recompute" /><input type="reset" value="Reset" /></p>
</form>
