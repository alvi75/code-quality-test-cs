public virtual void incrementSecondaryProgressBy(int delta){
    lock (this){
        mIndeterminate = false;
        mCurrentDrawable = mIndeterminateDrawable;
        mIndeterminateDuration = INDETERMINATE_DRAWABLE_TIMEOUT;
        startAnimation();
    }
}