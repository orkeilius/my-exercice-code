/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 */

import java.util.*;
// @lc code=start

class LRUCache {

    private int maxCapacity;
    private LinkedHashMap<Integer,Integer> cache;

    public LRUCache(int maxCapacity) {
        this.maxCapacity = maxCapacity;
        this.cache = new LinkedHashMap<Integer,Integer>(maxCapacity, 0.75f, true){
            protected boolean removeEldestEntry(Map.Entry eldest) {
                    return size() > maxCapacity;
                }
        };
    }
    
    public int get(int key) {
        return this.cache.getOrDefault( key, -1);
    }
    
    public void put(int key, int value) {
        this.cache.put(key,value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(cache);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

