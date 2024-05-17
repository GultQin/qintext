#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>
 
#define N 4   // 消费者或者生产者的数目
#define M 20 // 缓冲数目 
int in = 0;   // 生产者放置产品的位置
int out = 0; // 消费者取产品的位置 
char buff[M]; // 缓冲区 
int producter_id = 0;   //生产者id
int consumer_id = 0; //消费者id
 
/* 打印缓冲情况 */
void print()
{
int i;
for(i = 0; i < M; i++)
   printf("%c ", buff[i]);
printf("\n");
}
 
/* 生产者方法 */
void *producter()
{
int id = ++producter_id;
 
while(1)
{
   // 用sleep的数量可以调节生产和消费的速度
   sleep(2);
   char data;
   data=rand()%26+65;     
   in = in % M;
   printf("生产者进程%d在%2d位置产生数据%c: ", id,in,data);  
   buff[in] = data;  
   print();  
   ++in;
}
}
 
/* 消费者方法 */
void *consumer()
{
char data;
int id = ++consumer_id;
while(1)
{
   // 用sleep的数量可以调节生产和消费的速度
   sleep(1);
   out = out % M;
   data=buff[out];
   printf("消费者进程%d在%2d位置消费数据%c: ",id, out,data);   
   buff[out] = '*';
   print();
   ++out;
}
}
 
int main()
{
pthread_t p[N];
pthread_t c[N];
int i;
int ret[N];

for(i=0; i<M; i++)
   buff[i]='*';  //'*'表示空,初始化缓冲区
srand((int)time(NULL));
// 创建N个生产者线程
for (i = 0; i < N; i++)
{
   ret[i] = pthread_create(&p[i], NULL,(void*)producter, (void *)(&i));
   if(ret[i] != 0)
   {
    printf("producter %d creation failed \n", i);
    exit(1);
   }
}
//创建N个消费者线程
for(i = 0; i < N; i++)
{
   ret[i] = pthread_create(&c[i], NULL, (void*)consumer, NULL);
   if(ret[i] != 0)
   {
    printf("consumer %d creation failed\n", i);
    exit(1);
   }
}
//销毁线程
for(i = 0; i < N; i++)
{
   pthread_join(p[i],NULL);
   pthread_join(c[i],NULL);
}
exit(0);
}



