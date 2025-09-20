public virtual void IncrementProgressBy(int diff){
    lock (this){
        mIndeterminate = false;
        SetProgress(mProgress + diff);
        if (mIndeterminate && mProgress >= mMax){
            mCurrentDrawable = mIndeterminateDrawable;
            mState = mIndeterminateState;
        }
        else{
            if (!mIndeterminate){
                mCurrentDrawable = mProgressDrawable;
                mState = mProgressState;
            }
        }
    }