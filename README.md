#Chinese Documents Search Engine, IR 2015 Fall

##呼叫程式
`$ python search.py`<br>
(with python2.7)<br>
<br>

##功能
- 單詞搜尋
    - 回傳"@文件id@文件id$總次數"
    - ranking by 該詞彙於該篇文章出現次數
- 多詞搜尋
    - 回傳"@文件id@文件id"
    - ranking by 多詞彙於該篇文章出現比例(搜尋m個含有n個)
	- 比例相同則比較多詞彙總出現次數(n個共出現幾次)
- 距離搜尋
    - 回傳"@文件id@文件id"
    - ranking by 總出現次數
- 布林搜尋
    - 回傳"@文件id@文件id"
    - no ranking
<br>

##使用文件
- PositionalList.txt
    - 中文詞#文章ID$次數&位置-位置-位置#文章ID$次數&位置-位置-位置...@總次數
<br>

##處理過程
1.  將query字串存進"temp/query.txt"檔

    ex. 搜尋 "傳統 and not 表演 or 先生"，query.txt內容為 "傳統 and not 表演 or 先生"

2.  將query結果文章存進"temp/output.txt"

    ex. 結果格式: @文章@文章@文章
<br>

##Processing
- 文章標題依日期改為id由小到大放入articles
- TDmatrix.txt
    - 首行(文件id)： 1,2,3,4,5,6,7,8,9, ... ,1200<br>
    - 其餘(次數)： 中文,在id#1出現次數,在id#2出現次數,在id#3出現次數, ... , 在id#1200出現次數<br>


