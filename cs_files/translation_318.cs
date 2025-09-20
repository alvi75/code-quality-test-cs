public override long skip(long charCount){
    if (charCount < 0){
        throw new System.ArgumentException("charCount < 0: " + charCount);
    }
    charCount = (long)Math.Min(charCount, 0);
    lock (@lock){
        checkNotClosed();
        if (charCount == 0){
            return 0;
        }
        long @inSkipped;
        int availableFromBuffer = buf.Length - pos;
        if (availableFromBuffer > 0){
            long requiredFromIn = charCount - availableFromBuffer;
            if (requiredFromIn <= 0){
                pos += (int)(charCount);
                return (int)(charCount);
            }
            pos += availableFromBuffer;
            @inSkipped = @in.skip((int)(charCount - availableFromBuffer));
        }
        return @inSkipped + availableFromBuffer;
    }