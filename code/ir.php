<?php
$keyword=trim($_POST["keyword"]);
$input = fopen("../temp/query.txt" , "w");
fwrite($input , $keyword);
fclose($input);
$pyscript = './search.py';
$python = 'C:\\Python27\\python.exe';

$cmd = "$python $pyscript";
exec("$cmd" , $output);

$file = fopen("../temp/output.txt" , "r");
$str = "";
while (!feof($file)) {
            $str .= fgets($file);
        }
        fclose($file);
        if($str == "NOT FOUND")
        {
            echo "無搜尋結果<br>";
            return;
        }
        $qcount = strtok($str , '$');
        $qcount = strtok('$');
        if($qcount != "")
            echo "該單詞在文本資料庫中所出現的總次數為".$qcount."次<br>";
        $tok_str = strtok($str , '$');
        $tok_str = strtok($tok_str, '@');
        $count = 0;
        while($tok_str != false)
        {
            $count++;
            $topic = "";
            $temp = fopen("../articles/$tok_str.txt" , "r");
            $topic = fgets($temp);
            echo ("<font size=\"5\" </font><a  href=\"/IR/articles_transfer/$tok_str.txt  \"target=\"_self\">$count. $topic<br></a>");
            $snippet = fgets($temp);
            $snippet = fgets($temp);
            $snippet = fgets($temp);
            $snippet = fgets($temp);
            $snippet = fgets($temp);
            $snippet = fgets($temp);
            echo ("<font size=\"4\" </font>$snippet......<br><br>");
            fclose($temp);
            $tok_str = strtok('@');
        }
        echo $tok_str.'<br>';

?>
