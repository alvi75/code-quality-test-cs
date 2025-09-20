public override void AddAll(T[] src, int srcIdx, int srcCnt){
    while (0 < srcCnt){
        int i = tailBlkIdx;
        int n = Math.Min(srcCnt, BLOCK_SIZE - i);
        if (n == 0){
            AddItem(src[srcIdx++]);
            srcCnt--;
            continue;
        }
        System.Array.Copy(src, srcIdx, tailBlock, i, n);
        tailBlkIdx += n;
        size += n;
        srcIdx += n;
        srcCnt -= n;
    }
}