public virtual void FreeBefore(int pos){
    Debug.Assert(pos >= 0);
    Debug.Assert(pos <= outerInstance.nextPos);
    int newCount = outerInstance.nextPos - pos;
    Debug.Assert(newCount <= outerInstance.count, "newCount=" + newCount + " count=" + outerInstance.count);
    Debug.Assert(newCount <= outerInstance.buffer.Length, "newCount=" + newCount + " buf.length=" + outerInstance.buffer.Length);
    outerInstance.count = newCount;
}
}