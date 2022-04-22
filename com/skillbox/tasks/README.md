## Задача числа Фибоначчи:
```java
public class Fibonacci {

    public static void main(String[] args) {
        for (int i = 1, j = 1; i <= 200; i += j, j += i)
            System.out.print(i + " " + j + " ");
    }
}
```

## Задача числа-вампиры:

```java
package com.skillbox.tasks;

/**
 * https://en.wikipedia.org/wiki/Vampire_number
 */
public class VampireNumber {
    public static void main(String[] args) {
        String text = "";
        for (int i = 1; i < 100; i++)
            for (int j = 1; j < 100; j++) {
                int mult = i * j;
                if (mult > 1111) {
                    int e1 = mult % 10;
                    mult = mult / 10;
                    int e2 = mult % 10;
                    mult = mult / 10;
                    int e3 = mult % 10;
                    mult = mult / 10;
                    int e4 = mult % 10;

                    int i1 = i;
                    int f1 = i1 % 10;
                    i1 = i1 / 10;
                    int f2 = i1 % 10;

                    int i2 = j;
                    int g1 = i2 % 10;
                    i2 = i2 / 10;
                    int g2 = i2 % 10;

                    if (e4 == f2 || e4 == f1 || e4 == g2 || e4 == g1) {
                        if (e4 == f2)
                            f2 = 0;
                        else if (e4 == f1)
                            f1 = 0;
                        else if (e4 == g2)
                            g2 = 0;
                        else if (e4 == g1)
                            g1 = 0;

                        if (e3 == f2 || e3 == f1 || e3 == g2 || e3 == g1) {
                            if (e3 == f2)
                                f2 = 0;
                            else if (e3 == f1)
                                f1 = 0;
                            else if (e3 == g2)
                                g2 = 0;
                            else if (e3 == g1)
                                g1 = 0;

                            if (e2 == f2 || e2 == f1 || e2 == g2 || e2 == g1)
                                if (e2 == f2)
                                    f2 = 0;
                                else if (e2 == f1)
                                    f1 = 0;
                                else if (e2 == g2)
                                    g2 = 0;
                                else if (e2 == g1)
                                    g1 = 0;

                            if (e1 == f2 || e1 == f1 || e1 == g2 || e1 == g1)
                                if (e2 == f2)
                                    f2 = 0;
                                else if (e2 == f1)
                                    f1 = 0;
                                else if (e2 == g2)
                                    g2 = 0;
                                else if (e2 == g1)
                                    g1 = 0;

                            if (e1 == f2 || e1 == f1 || e1 == g2 || e1 == g1)
                                if (e1 == f2)
                                    f2 = 0;
                                else if (e1 == f1)
                                    f1 = 0;
                                else if (e1 == g2)
                                    g2 = 0;
                                else if (e1 == g1)
                                    g1 = 0;

                            if (f2 == 0 && f1 == 0 && g2 == 0 && g1 == 0)
                                text += "" + e4 + e3 + e2 + e1 + "-";
                        }
                    }
                }
            }
        String[] arrayAll = text.split("-");
        String result = "";
        for (String s : arrayAll)
            if (!result.contains(s))
                result += s + ", ";
        result = result.substring(0, result.length() - 2);
        result += ".";
        System.out.println(result);
    }
}
```