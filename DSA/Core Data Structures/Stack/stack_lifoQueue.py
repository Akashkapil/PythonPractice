# using lifo queue

# slower than deque and list , its thread safe.
from queue import LifoQueue

st = LifoQueue()

st.put("a")
st.put("b")
st.put("c")

print(st.get())
print(st.get())