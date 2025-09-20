public virtual void setMax(int max){
    lock (this){
        if (max < 0){
            throw new System.ArgumentException("max must be >= 0");
        }
        if (max != mMax){
            mMax = max;
            postInvalidate();
            if (mProgress > max){
                mProgress = max;
            }
            refreshProgress(android.@internal.R.id.progress, mProgress, false);
        }
    }
}
}