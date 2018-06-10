import numpy as np

def intersection():
    p = np.array([0, 0])
    r = np.array([1, 1])
    q = np.array([0.1, 0.1])
    s = np.array([.1, .1])

    if np.cross(r, s) == 0 and np.cross((q-p), r) == 0:   

        t0 = np.dot(q-p, r)/np.dot(r, r)
        t1 = t0 + np.dot(s, r)/np.dot(r, r)
        print(t1, t0)
        if ((np.dot(s, r) > 0) and (0 <= t1 - t0 <= 1)) or ((np.dot(s, r) <= 0) and (0 <= t0 - t1 <= 1)):
            print('collinear and overlapping, q_s in p_r')
        else:
            print('collinear and disjoint')
    elif np.cross(r, s) == 0 and np.cross((q-p), r) != 0: 
        print('parallel')
    else:
        t = np.cross((q - p), s) / np.cross(r, s)
        u = np.cross((q - p), r) / np.cross(r, s)
        if 0 <= t <= 1 and 0 <= u <= 1:
          
            print('intersection: ', p + t*r)
        else:
            print('not parallel and not intersect')


def point2segment():
    p = np.array([-1, 1])    
    a = np.array([0, 1])    
    b = np.array([1, 0])    
    ab = b-a    
    ap = p-a
    distance = np.abs(np.cross(ab, ap)/np.linalg.norm(ab))  
    print(distance)

    
    bp = p-b
    cosTheta1 = np.dot(ap, ab) / (np.linalg.norm(ap) * np.linalg.norm(ab))
    theta1 = np.arccos(cosTheta1)
    cosTheta2 = np.dot(bp, ab) / (np.linalg.norm(bp) * np.linalg.norm(ab))
    theta2 = np.arccos(cosTheta2)
    if np.pi/2 <= (theta1 % (np.pi*2)) <= 3/2 * np.pi:
        print('out of a')
    elif -np.pi/2 <= (theta2 % (np.pi*2)) <= np.pi/2:
        print('out of b')
    else:
        print('between a and b')



if __name__ == '__main__':
    point2segment()

