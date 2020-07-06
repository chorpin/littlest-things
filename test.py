def findSubstring(s, words):
    step = len(words[0])
    L = 0
    R = 0
    # init dict
    dic = {}
    result = []
    critia = len(words) * step
    for word in words:
        dic[word] = [0, 0]
    for i in range(0, len(s)):
        if i > (len(s) - step):
            break
        ss = s[i:i+step]
        if s[i:i + step] in dic:
            while i < (len(s)-step):
                if (s[i:i + step] in dic) :
                    if dic[s[i:i + step]][0] == 0:
                        dic[s[i:i+step]][1] = i
                        R = R + step
                        dic[s[i:i+step]][0] = 1
                        for h in dic:
                            if dic[h][1] < L:
                                dic[h][0] = 0
                        if (R - L) == critia:
                            result.append(L)
                            #for h in dic:
                                #dic[h][0] = 0
                    else:
                        L = dic[s[i:i+step]][1] + step
                        R = R + step
                        dic[s[i:i + step]][0] = 1
                        dic[s[i:i + step]][1] = i
                        for h in dic:
                            if dic[h][1] < L:
                                dic[h][0] = 0
                        if (R - L) == critia:
                            result.append(L)
                            #for h in dic:
                                #dic[h][0] = 0

                else:
                    L = i + step
                    R = L
                    for h in dic:
                        if dic[h][1] < L:
                            dic[h][0] = 0
                i = i + step
        else:
            continue
    return result
r = findSubstring('barfoofoobarthefoobarman', ['the', 'foo', 'bar'])
print(r)




