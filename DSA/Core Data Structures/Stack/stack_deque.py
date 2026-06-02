# stack using collection.deque class
# deque is faster than list for large data operations
from collections import deque

st = deque()
st.append('a')
st.append('b')
st.append('c')

print(st)
print(st.pop())
print(st.pop())