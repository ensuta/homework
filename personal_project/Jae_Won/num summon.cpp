#include <stdio.h>

int main()
{
    int num,hap=0,ans;
    printf("계산기\n\n");
    printf("숫자를 몇번 더 할 건가요:");
    scanf("%d",&num);
    // 숫자를 몇번 더할 지 묻기
    for(int a=0; a<num; a++){
        printf("%d번째로 더할 숫자를 입력하세요",a+1);
        scanf("%d",&ans);
        // 더할 숫자 입력
       hap=hap+ans;        
    }
    
    printf("%d번째 숫자까지 더한 값은: %d",num,hap);
    //결과 출력
    return 0;
}


