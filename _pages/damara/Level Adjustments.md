!!How to buy off Level Adjustments

You can use XP to buy off level adjustments as detailed in Unearthed Arcana ([http://www.d20srd.org/srd/variant/races/reducingLevelAdjustments.htm|Reducing Level Adjustments]). However, the system is somewhat complicated. Since extra XP in Damara is purchased for 5 gold per 1 XP, we provide the following handy table.

The table is written for characters with no monster hit dice. If you have monster HD, add 5,000 gp times the number of HD to each table value. For example, if you are a gnoll, you have two monster HD, so each buy-off entry costs 10,000 gp more.

||__Starting Level Adjustment__|__Minimum Class Level__|__Cost__

1|3|15,000 gp

2|6|35,000 gp
|9|45,000 gp

3|9|55,000 gp
|15|80,000 gp
|18|90,000 gp

4|12|75,000 gp
|21|115,000 gp
|27|140,000 gp
|30|150,000 gp

5|15|95,000 gp
|27|150,000 gp
|36|190,000 gp
|42|215,000 gp
|45|225,000 gp

6|18|115,000 gp
|33|185,000 gp
|45|240,000 gp
|54|280,000 gp
|60|305,000 gp
|63|315,000 gp

7|21|135,000 gp
|39|220,000 gp
|54|290,000 gp
|66|345,000 gp
|75|385,000 gp
|81|410,000 gp
|84|420,000 gp

8|24|155,000 gp
|45|255,000 gp
|63|340,000 gp
|78|410,000 gp
|90|465,000 gp
|99|505,000 gp
|105|530,000 gp
|108|540,000 gp

9|27|175,000 gp
|51|290,000 gp
|72|390,000 gp
|90|475,000 gp
|105|545,000 gp
|117|600,000 gp
|126|640,000 gp
|132|665,000 gp
|135|675,000 gp

10|30|195,000 gp
|57|325,000 gp
|81|440,000 gp
|102|540,000 gp
|120|625,000 gp
|135|695,000 gp
|147|750,000 gp
|156|790,000 gp
|162|815,000 gp
|165|825,000 gp
||
Wow, you actually scrolled all the way down here. Here's your reward:
{TAG(tag=&gt;pre)}~np~public class LA {
  public static void main(String[] args) {
    int mult = 5; // 1 XP = 5 gp
    System.out.println(
      &quot;||__Starting Level Adjustment__|__Minimum Class Level__|__Cost__&quot;);
    for (int la=1; la&lt;=10; la++) {
      System.out.println();
      System.out.print(la);
      int lev = 3 * la;
      for (int left=la; left&gt;0; left--) {
        int gp = (lev + left - 1) * 1000 * mult;
        String s = &quot;&quot; + gp;
        s = s.substring(0, s.length() - 3) + &quot;,&quot; + s.substring(s.length() - 3);
        System.out.println(&quot;|&quot; + lev + &quot;|&quot; + s + &quot; gp&quot;);
        lev += 3 * (left - 1);
      }
    }
  }
}~/np~{TAG}
