public override void Run(){
    long lastReopenStartNS = Time.NanoTime();
    while (!m_stop){
        while (!m_stop){
            lock (this){
                bool hasWaiting = m_waitingGen > m_searchingGen;
                if (hasWaiting){
                    m_reopenCond.Set();
                }
                m_lastNS = Time.NanoTime();
                m_searchingGen = m_searchingGen + 1;
                m_recalcPending = true;
            }
        }
    }