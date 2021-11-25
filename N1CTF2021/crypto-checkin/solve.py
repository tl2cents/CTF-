from Crypto.Util.number import *
from z3 import *
n = 124592923216765837982528839202733339713655242872717311800329884147642320435241014134533341888832955643881019336863843062120984698416851559736918389766033534214383285754683751490292848191235308958825702189602212123282858416891155764271492033289942894367802529296453904254165606918649570613530838932164490341793
c = 119279592136391518960778700178474826421062018379899342254406783670889432182616590099071219538938202395671695005539485982613862823970622126945808954842683496637377151180225469409261800869161467402364879561554585345399947589618235872378329510108345004513054262809629917083343715270605155751457391599728436117833
h = 115812446451372389307840774747986196103012628652193338630796109042038320397499948364970459686079508388755154855414919871257982157430015224489195284512204803276307238226421244647463550637321174259849701618681565567468929295822889537962306471780258801529979716298619553323655541002084406217484482271693997457806
p0 = 4055618
q0 = 0b101101110111111001010
a=2021
b=1120
e = 65537
# x^2 -hx + 1 = 0 mod n
            
def exploit():
    R = Zmod(n)
    PR.<x> = PolynomialRing(R)
    _x = 2021*p0*2^490 + 1120*q0*2^491 + x
    f = (_x^2 - _x*h + 1).monic()
    # [7279473437564993427256268527891542563557232159626049883951364173102121134158423609775502464752174435483615142675582269470774951285125088232851515513237]
    # 726 s
    roots = f.small_roots(X=2^505,epsilon=1/80)
    print(roots)


if __name__ == "__main__":
    # exploit()
    q1=n//(p0<<490)
    q0=q1>>491
    x=7279473437564993427256268527891542563557232159626049883951364173102121134158423609775502464752174435483615142675582269470774951285125088232851515513237
    S=Solver()
    _p=BitVec('_p',1080)
    _q=BitVec('_q',1080)
    S.add((_p*_q)==(n*2021*1120))
    S.add((_p+_q)==(1120*q0*2**491+2021*p0*2**490+x))
    ans=S.check()
    print(S.model())
    p=S.model()[_p].as_long()//2021
    q=S.model()[_q].as_long()//1120
    assert p*q==n
    phi=(p-1)*(q-1)
    d=inverse(e,phi)
    flag=pow(c,d,n)
    print(long_to_bytes(flag))
    # n1ctf{093fd4c4-5cc9-427e-98ef-5a04914c8b4e}