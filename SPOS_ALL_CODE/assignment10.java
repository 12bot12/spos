import java.io.*;
import java.util.*;
public class page_replacement{
static void lru(){
int n,fsize,page_faults=0,page_hit=0;
Scanner sc = new Scanner(System.in);
System.out.println("Enter the number of pages to be entered");
n = sc.nextInt();
HashSet<Integer> s = new HashSet<>(n);
HashMap<Integer, Integer> indexes = new HashMap<>();
int pages[] = new int[n];
System.out.println("Enter the frame size ");
fsize = sc.nextInt();
System.out.println("Enter the pages ");
for(int i=0;i<n;i++){
pages[i] = sc.nextInt();
}
for(int i=0;i<n;i++) {
if(s.size() < fsize) {
if (!s.contains(pages[i])) {
s.add(pages[i]);
page_faults++;
}
else
{
page_hit++;
}
indexes.put(pages[i], i);
}
else {
int lru = Integer.MAX_VALUE, val=Integer.MIN_VALUE;
Iterator<Integer> itr = s.iterator();
while (itr.hasNext()) {
int temp = itr.next();
if (indexes.get(temp) < lru)
{

lru = indexes.get(temp);
val = temp;

}
}
s.remove(val);
s.add(pages[i]);

indexes.put(pages[i], i);
}
System.out.println(s);
}
System.out.println("Page Hit: "+ page_hit);
System.out.println("Page Fault: " +page_faults);
System.out.println("Hit ratio: "+(float)((float)page_hit/n));
}
static void optimal(){
Scanner sc=new Scanner(System.in);
int frames, pointer = 0, hit = 0, fault = 0,ref_len;
boolean isFull = false;
int buffer[];
int reference[];
int mem_layout[][];
System.out.println("Please enter the number of Frames: ");
frames = sc.nextInt();
System.out.println("Please enter the length of the Reference string: ");
ref_len =sc.nextInt();
reference = new int[ref_len];
mem_layout = new int[ref_len][frames];
buffer = new int[frames];
for(int j = 0; j < frames; j++)
buffer[j] = -1;
System.out.println("Please enter the reference string: ");
for(int i = 0; i < ref_len; i++)
{
reference[i] =sc.nextInt();
}
System.out.println();
for(int i = 0; i < ref_len; i++)
{
int search = -1;
for(int j = 0; j < frames; j++)
{
if(buffer[j] == reference[i])
{
search = j;
hit++;
break;
}
}
if(search == -1)
{
if(isFull)
{
int index[] = new int[frames];
boolean index_flag[] = new boolean[frames];
for(int j = i + 1; j < ref_len; j++)
{
for(int k = 0; k < frames; k++)

{
if((reference[j] == buffer[k]) &&

(index_flag[k] == false))

{
index[k] = j;
index_flag[k] = true;
break;
}
}
}
int max = index[0];
pointer = 0;
if(max == 0)
max = 200;
for(int j = 0; j < frames; j++)
{
if(index[j] == 0)
index[j] = 200;
if(index[j] > max)
{
max = index[j];
pointer = j;
}
}
}
buffer[pointer] = reference[i];
fault++;
if(!isFull)
{
pointer++;
if(pointer == frames)
{
pointer = 0;
isFull = true;
}
}
}
for(int j = 0; j < frames; j++)
mem_layout[i][j] = buffer[j];

}
/*for(int i = 0; i < frames; i++)
{
for(int j = 0; j < ref_len; j++)
System.out.printf("%3d ",mem_layout[j][i]);
System.out.println();
}*/
System.out.println("Number of Hits: " + hit);
System.out.println("Hit Ratio: " + (float)((float)hit/ref_len));
System.out.println("Number of Faults: " + fault);

}

public static void main(String[] args){
int choice=0;
Scanner sc=new Scanner(System.in);
System.out.println("\n*******************Menu********************\n");
System.out.println("\n1.Least Recently Used Algorithm");
System.out.println("\n2.Optimal Algorithm");
System.out.println("\nplease enter your choice:");
choice=sc.nextInt();
switch(choice){
case 1:
lru();
break;
case 2:
optimal();
break;
default:
System.out.println("\n Sorry! You have entered a wrong choice");
}
}

}
