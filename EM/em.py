'''
@version 0.1
@date 2016-05-01
@author yangmu
'''

import math

[pi,p,q]=[0.4,0.6,0.7]

x=[1,1,0,1,0,0,1,0,1,1]

def cal_u(pi1,p1,q1,xi):
    return pi1*math.pow(p1,xi)*math.pow(1-p1,1-xi)/float(pi1*math.pow(p1,xi)*math.pow(1-p1,1-xi)+(1-pi1)*math.pow(q1,xi)*math.pow(1-q1,1-xi))

def e_step(pi1,p1,q1,x):
    return [cal_u(pi1,p1,q1,xi) for xi in x]

def m_step(u,x):
    pi1=sum(u)/len(u)
    p1=sum([u[i]*x[i] for i in range(len(u))]) / sum(u)
    q1=sum([(1-u[i])*x[i] for i in range(len(u))]) / sum([1-u[i] for i in range(len(u))])
    return [pi1,p1,q1]

def run(start_x,start_pi,start_p,start_q,iter_num):
    for i in range(iter_num):
        u=e_step(start_pi,start_p,start_q,x)
        print i,[start_pi,start_p,start_q]
        if [start_pi,start_p,start_q]==m_step(u,x):
            break
        else:
            [start_pi,start_p,start_q]=m_step(u,x)

if __name__=='__main__':
    run(x,pi,p,q,100)