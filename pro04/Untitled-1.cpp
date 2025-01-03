#include<iostream>
#include<memory.h>
using namespace std;

//此题本质是看图中是否有奇数边形

bool Color(int** array, int n, int start, int color){
    bool flag = true;
    if(array[start][start]==0){//没有被涂色
        array[start][start] = color;//涂上指定的颜色
        for(int i=0;i<=n;i++){//遍历自己以外的所有点
            if(i==start){continue;}
            if(array[start][i]){//遍历到的冲突点
                flag = Color(array,n,i,-color);//尝试涂反色
            }
        }
    }
    else{//涂上了颜色
        flag = (array[start][start] == color);//检查是否颜色冲突
        //注意 任何被涂色的元素都递归调用了Color，因此与其相连的元素一定都被上过了颜色，不必继续追究下去
    }
    return flag;
}

int main(){
    int n,k;
    cin >> n >> k;

    int** array = new int*[n];
    for (int i=0;i<n;i++){
        array[i] = new int[n];
    }
    for(int j=0;j<n;j++){
        for(int k=0;k<n;k++){
            array[j][k]=0;
        }
    }

    //array[x][y] 置1表示x与y相连
    //array[x][x] 0表示未涂色，1和-1分别是两种颜色

    int a,b;
    for(int i=0;i<k;i++){
        cin >> a >> b;
        a--;
        b--;
        array[a][b] = 1;
        array[b][a] = 1;
    }

    bool flag = true;
    for(int i=0;i<n;i++){
        if(array[i][i]==0){
            flag = Color(array,n-1,i,1);
            if(!flag){break;}
        }
    }

    if(flag){cout << "true" << endl;}
    else{cout << "false" << endl;}
    
    return 0;

}