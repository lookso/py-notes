<?php
function phpfab($max){
    $n=0;
    $a=0;
    $b=1;
    while ($n < $max){
        // 注意python的 a,b=b,a+b 和 a=b b=a+b 的区别
        // https://blog.csdn.net/qq_41187256/article/details/79687084

        // goroutine和yield区别：https://segmentfault.com/q/1010000011073517
        yield $b;
        $c=$a+$b;
        $a=$b;
        $b=$c;
        $n = $n + 1;
    }
}
foreach (phpfab(5) as $range) {
    echo "Dataset {$range}\n";
}
?>