//prime ring
#include<iostream>
using namespace std;


bool isPrime(int n){
    if(n==1) return false;
    for(int i=2;i*i<=n;i++){
        if(n%i==0) return false;
    }
    return true;
}

int main(){
    int n;
    int a[20];
    int vis[20];
    int cnt=0;
    while(cin>>n){
        cnt++;
        cout<<"Case "<<cnt<<":"<<endl;
        for(int i=1;i<=n;i++){
            a[i]=i;
            vis[i]=0;
        }
        vis[1]=1;
        int i=1;
        while(i<=n){
            if(i==n){
                if(isPrime(a[1]+a[n])){
                    for(int j=1;j<=n;j++){
                        cout<<a[j];
                        if(j!=n) cout<<" ";
                    }
                    cout<<endl;
                }
                i--;
                vis[a[i]]=0;
                i--;
                vis[a[i]]=0;
                a[i]++;
            }
            else{
                a[i]++;
                if(a[i]<=n&&vis[a[i]]==0&&isPrime(a[i]+a[i-1])){
                    vis[a[i]]=1;
                    i++;
                }
            }
        }
        cout<<endl;
    }
    return 0;
} 

