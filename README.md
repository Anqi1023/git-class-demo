# Git Class Demo - Study Checklist

A small Python command-line project for practicing Git and GitHub.

**Student:** Dong anqi  
**GitHub:** [Anqi1023](https://github.com/Anqi1023)

## Features

- Add a study task.
- List tasks and their completion status.
- Mark a task as completed.
- Save tasks locally between runs.

## Requirements

Python 3.9 or newer. No third-party packages are needed.

## Run the project

Download or clone this repository, open a terminal in the project folder, and run:

```bash
python main.py add "Learn Git basics"
python main.py add "Practice a GitHub commit"
python main.py list
python main.py done 1
python main.py list
```

On systems where Python is named `python3`, replace `python` with `python3`.

After these commands, the task list is:

```text
1. [x] Learn Git basics
2. [ ] Practice a GitHub commit
```

Use `python main.py --help` to view the commands. Task numbers start at 1.
Personal tasks are saved in `tasks.json`, which is excluded from Git tracking.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Study checklist program |
| `README.md` | Project introduction and instructions |
| `notes.txt` | Git command reference for this exercise |
| `.gitignore` | Excludes local task data and temporary files |

## Learning goals

Practice creating a repository, tracking source files, making commits, and
sharing a GitHub project link. This is a separate introductory practice project.

## 中文说明

这是一个独立的 Git 与 GitHub 入门练习项目，功能是管理学习任务清单。
可以添加任务、查看列表、标记完成；任务会保存在本地，下次运行时继续使用。
在项目文件夹中打开终端，按照上面的命令运行即可，不需要安装额外的 Python 库。

## Acknowledgment

Prepared with AI assistance for learning and practice.
