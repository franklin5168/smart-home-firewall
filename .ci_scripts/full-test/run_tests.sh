EXITCODE=0
VALGRIND_SUPP="$GITHUB_WORKSPACE/.ci_scripts/full-test/valgrind.supp"

PREFIX=""
for file in $GITHUB_WORKSPACE/bin/test/*
do
    if [[ "$file" == *"rule_utils-test" ]]
    then
        PREFIX="sudo"
    fi
    if [[ $# -eq 1 && $1 == valgrind ]]
    then
        $PREFIX valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all --suppressions="$VALGRIND_SUPP" --error-exitcode=1 "$file"
    else
        $PREFIX "$file"
    fi
    # If the exit code is not 0, set EXITCODE to 1
    if [[ $? -ne 0 ]]
    then
        EXITCODE=1
    fi
done

exit $EXITCODE
