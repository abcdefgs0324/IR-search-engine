#Chinese Documents Search Engine, IR 2015 Fall

##�I�s�{��
`$ python search.py`<br>
(with python2.7)<br>
<br>

##�\��
- ����j�M
    - �^��"@���id@���id$�`����"
    - ranking by �ӵ��J��ӽg�峹�X�{����
- �h���j�M
    - �^��"@���id@���id"
    - ranking by �h���J��ӽg�峹�X�{���(�j�Mm�ӧt��n��)
	- ��ҬۦP�h����h���J�`�X�{����(n�Ӧ@�X�{�X��)
- �Z���j�M
    - �^��"@���id@���id"
    - ranking by �`�X�{����
- ���L�j�M
    - �^��"@���id@���id"
    - no ranking
<br>

##�ϥΤ��
- PositionalList.txt
    - �����#�峹ID$����&��m-��m-��m#�峹ID$����&��m-��m-��m...@�`����
<br>

##�B�z�L�{
1.  �Nquery�r��s�i"temp/query.txt"��

    ex. �j�M "�ǲ� and not ��t or ����"�Aquery.txt���e�� "�ǲ� and not ��t or ����"

2.  �Nquery���G�峹�s�i"temp/output.txt"

    ex. ���G�榡: @�峹@�峹@�峹
<br>

##Processing
- �峹���D�̤���אּid�Ѥp��j��Jarticles
- TDmatrix.txt
    - ����(���id)�G 1,2,3,4,5,6,7,8,9, ... ,1200<br>
    - ��l(����)�G ����,�bid#1�X�{����,�bid#2�X�{����,�bid#3�X�{����, ... , �bid#1200�X�{����<br>


