
def isPalindrome(st):
    st = st.lower
    sl = 0
    for c in st:
          sl += 1
    for i in range(sl):
        if st[i] == " " or st[i] == ":" or st[i] == "," or st[i] == "'":
                st = st.replace(st[i], "")
        else:
                continue
    return st

a = input("s: ")

isPalindrome(a)