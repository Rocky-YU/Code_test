# Code_test
# GitHub 教程
1、Fork：可以理解为“拉分支”，如果我们对某一个项目比较感兴趣，并且想在此基础之上开发新的功能，这时我们就可以Fork这个项目，这表示复制一个完成相同的项目到我们的 GitHub 账号之中，而且独立于原项目。之后，我们就可以在自己复制的项目中进行开发了。
2、Pull Request：可以理解为“提交请求”，此功能是建立在Fork之上的，如果我们Fork了一个项目，对其进行了修改，而且感觉修改的还不错，我们就可以对原项目的拥有者提出一个Pull请求，等其对我们的请求审核，并且通过审核之后，就可以把我们修改过的内容合并到原项目之中，这时我们就成了该项目的贡献者。
3、Merge：可以理解为“合并”，如果别人Fork了我们的项目，对其进行了修改，并且提出了Pull请求，这时我们就可以对这个Pull请求进行审核。如果这个Pull请求的内容满足我们的要求，并且跟我们原有的项目没有冲突的话，就可以将其合并到我们的项目之中。当然，是否进行合并，由我们决定。
4、Watch：可以理解为“观察”，如果我们Watch了一个项目，之后，如果这个项目有了任何更新，我们都会在第一时候收到该项目的更新通知。
5、Gist：如果我们没有项目可以开源或者只是单纯的想分享一些代码片段的话，我们就可以选择Gist。不过说心里话，如果不翻墙的话，Gist并不好用。



# Git 的相关指令
git init 其作用就是初始一个 Git 仓库
it status命令，查看仓库的状态.
git add hit.txt命令，将hit.txt文件添加到 Git 仓库.
git commit -m "text commit"命令，将hit.txt文件提交到 Git 仓库.
git log"命令，打印 Git 仓库提交日志。
git branch命令，查看 Git 仓库的分支情况。
git checkout a命令，切换到a分支。
git merge a命令，将a分支合并到master分支，前提是先切回到master分支。
git branch -d a命令，删除a分支。（也是需要先切回其它分支，不能在该分支下删除该分支）
git tag v1.0命令，为当前分支添加标签。
git branch testbranch 创建分支testbranch
git checkout testbranch 切换到分支testbranch
git push origin testbranch 在分支testbranch环境下，使用该命令，同步到GitHub。如果在其它分支则 git push origin 其它分支
git merge  命令时用来合并的，而合并的对象就是branch（分支）
git pull 
git fetch  将本地分支与远程保持同步
git fetch --all  将本地所有分支与远程保持同步
git pull --all  拉取所有分支代码






# Git中分支解释
  https://blog.csdn.net/xiaoxuantengkong/article/details/45231331

