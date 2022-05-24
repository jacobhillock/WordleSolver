CWD=$(pwd)
cd $( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ../

python3.10 console.py $@

cd $CWD