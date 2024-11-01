import re

f = open('access.log', 'r',encoding='utf-8')
lines = f.readlines()
flag_dic = {}

for line in lines:
    matchObj = re.search(r"1andif\(substr\(\(selectflagfromsqli.flag\),(.*?),1\)='(.*?)',1,\(", line)
    #  FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=0x6265617574795f7061726c6f7572 LIMIT 2,1\),(.*？),1\)\)>(.*?),0,1
    # \(IF\(ORD\(MID\(\(SELECT DISTINCT\(IFNULL\(CAST\(schema_name AS NCHAR\),0x20\)\) FROM INFORMATION_SCHEMA.SCHEMATA LIMIT 0,1\),(.*?),1\)\)>(.*?)
    # FROM beauty_parlour.femaleinfo WHERE pinyin=0x707579616e LIMIT 0,1\),(.*?),1\)\)>(.*?),0,1
    # matchObj = re.search(r"var_dump\(ord\(file_get_contents\('maybeinthisfile.php'\)\[(.*?)\]\)==(.*?)\);\n", line)
    # from user\),(.*?),1\)\)=(.*?),sleep\(1\),1\)
    # var_dump\(ord\(file_get_contents\('maybeinthisfile.php'\)[(.*?)]\)==(.*?)\);
    #1andif\(substr\(\(selectflagfromsqli.flag\),(.*?),1\)='(.*?)',1,\(
    # \(CAST\(mail AS NCHAR\),0x20\) FROM beauty_parlour.femaleinfo WHERE pinyin=0x707579616e LIMIT 0,1\),(.*?),1\)\)>(.*?),0,1\)
    if matchObj:
        print(matchObj[2])
        key = matchObj[1]
        value = matchObj[2]
        flag_dic[key] = value
        print(flag_dic.values())
flag = ''
for value in flag_dic.values():
    flag += value
print(flag)