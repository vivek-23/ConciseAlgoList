class Solution
{
    public int find_median(int[] v)
    {
        PriorityQueue<Integer> min = new PriorityQueue<Integer>(100, (a,b) -> (a - b));
        PriorityQueue<Integer> max = new PriorityQueue<Integer>(100, (a, b) -> (b - a));
        for(int x : v){
           max.offer(x);
            while(max.size() - min.size() > 1){
                min.offer(max.poll());       
            }
            if(!min.isEmpty() && min.peek() < max.peek()){
                int temp = max.poll();
                max.offer(min.poll());
                min.offer(temp);
            }
        }
        
        if(v.length % 2 == 0) return (max.poll() + min.poll()) / 2;
        return max.poll();
    }
}
