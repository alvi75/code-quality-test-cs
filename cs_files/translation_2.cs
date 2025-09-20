public override void WriteByte(byte b){
    if (upto == blockSize){
        if (currentBlock != null){
            blocks.Add(currentBlock);
            blockEnd.Add(upto);
        }
        bAvail.Add(blockSize - upto);
    }
    else{
        AddBlock();
    }
}
bAvail.Add(8192);
}
}
currentBlock[upto++] = b;
}