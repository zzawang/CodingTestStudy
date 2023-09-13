#include <stdio.h>
#include <stdlib.h>
#define SIZE 300000

typedef struct Stack{
    int top;
    int data[SIZE];
}Stack;

void init(Stack* s){
    s->top=-1;
}

void push(Stack* s,int p){
    s->data[++(s->top)]=p;
}

int pop(Stack* s){
    if(s->top==-1){
        printf("스택공백에러");
        return 0;
    }
    return s->data[(s->top)--];
}

int main() {
    Stack s[6];
    for(int i=0;i<6;i++){
        init(&s[0]);
    }
    int ntest,j,pnum,p,count=1,n=0;
    scanf("%d %d",&ntest,&pnum);
    scanf("%d %d",&j,&p);
    push(&s[j-1],p);
    for(int i=1;i<ntest;i++){
        scanf("%d %d",&j,&p);
        if(s[j-1].data[s[j-1].top]>p){
            while(s[j-1].data[s[j-1].top]>p){
                n=pop(&s[j-1]);
                count++;
            }
            if(s[j-1].top==-1){
                push(&s[j-1],p);
                count++;
                continue;
            }
            if(s[j-1].data[s[j-1].top]<p){
                push(&s[j-1],p);
                count++;
                continue;
            }
            else
                continue;
        }
        else if(s[j-1].data[s[j-1].top]<p){
            push(&s[j-1],p);
            count++;
        }
        else
            continue;
    }
    printf("%d\n",count);
    return 0;
}