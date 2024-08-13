def git_control(branch_or_tag, startdate, enddate, code_path):

    if startdate:
        from youqu_git_commit.check import check_git_installed
        from youqu_git_commit.code_statistics import CodeStatistics

        check_git_installed()
        CodeStatistics(branch_or_tag, startdate, enddate, code_path).codex()
    else:
        print("-s/--startdate 参数未传入")
