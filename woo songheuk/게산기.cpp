#include <stdio.h>

int main()
{
    int num,hap=0,ans;
    printf("숫자를 몇번 더 할 건가요:");
    scanf("%d",&num);
    for(int a=0; a<num; a++){
        printf("%d번째로 더할 숫자를 입력하세요",a+1);
        scanf("%d",&ans);
        hap=hap+ans;
    }
    
    printf("%d번째 숫자까지 더하나 값은: %d",num,hap);

    return 0;
}
