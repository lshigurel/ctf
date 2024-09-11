# rsa14exp.py
from Crypto.Util.number import *
from gmpy2 import gcdext
import math
n = 18643499005185370330995708811783449898344018016270097409913582783808809605518646828631454959712233397595316274512830945122000020143752393112036637682392327568269875557951317541353170214890939828817996422521668702086297242340338386024529456457864475765895832977251489063394795566812975864820600883549303387586118614692339084159473653677925115502509507230834643803310477628260007500522821466371859471458699948271681412173397316718828689631234096138696397961628187227865869376440731230301503639175718854829427445165821260564891640040358584011694138047242267368482772460708343005077771678465916348241021632581055324846999
e1 = 18215
c1 = 10629723808188529311899383835949431828016458531560846566803528039150582746975227672434422012841603610175660419680251090129803113679778871122284628087683443030361610210844876497997930605567898121797413328688967285434198154005005800915404628333749097281814160932968639956587456053314940648648476121981772760400840642595803320996973877419613052652542998012080849944845314006211772667384433015934339456981772453731360169605566493925616678544981090055752968285667104395945404142516281889671845075967649153153186813220089487946780554444626492455916396580855916342652760507825705526990806619657461649191387382408908754157736
e2 = 12745
c2 = 15009624721284427735987272341975076070469303129128174990270347562042350201924789842609129477202805481999335512703591037965271220642601506282328363643589145980803521157125271912112543652976785292957779827494168181356020923531823192381541994851603755654682944457648950724751626979566848133817293330325059702990400623445353070263826918804849128049603457605982264055347595170562151414951348386759248390868956824384801929088295583278281226239799777949194036445066164670454021449842198795016855582726995098562660662247840048478115026477894819184756192092771053243449770544050403129271803511252438544836921835829040586644306

e1= math.pow(e1,1/5)
e2= math.pow(e2,1/5)
_, s1, s2 = gcdext(e1, e2)
m = pow(c1, s1, n) * pow(c2, s2, n) % n
flag = long_to_bytes(m)
print(flag)