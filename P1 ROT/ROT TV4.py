
import uncertainties as u


def func (J1,J2,J3,L1,L2,L3):



    return (J1*(L1**2 /((L1**2 + L2**2 + L3**2)))) + (J2*(L1**2 /((L1**2 + L2**2 + L3**2)))) + (J3*(L1**2 /((L1**2 + L2**2 + L3**2))))


a = func(0.00335,0.00169,0.00230,0.051,0.103,0.072)
b=func()


print(a)


