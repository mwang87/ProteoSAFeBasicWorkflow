echo "cp tool.xml $1/worker/conf/tool.xml"
cp tool.xml $1/worker/conf/tool.xml
echo "mkdir $1/workflows/basicworkflow"
mkdir $1/workflows/basicworkflow
echo "cp basicworkflow/* $1/workflows/basicworkflow/"
cp basicworkflow/* $1/workflows/basicworkflow/
echo "mkdir $1/tools/basicworkflow"
mkdir $1/tools/basicworkflow
echo "cp bin/basictool.py $1/tools/basicworkflow/"
cp bin/basictool.py $1/tools/basicworkflow/
