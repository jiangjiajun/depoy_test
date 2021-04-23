rm -rf cpp_results
mkdir cpp_results

infer_bin=$1

model_dir="det/models/YOLOv3-DarkNet"
echo "======Test model $model_dir======"
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --model_type=det 1>cpp_results/yolov3.txt 2>err
python det/script/diff.py cpp_results/yolov3.txt det/py_results/yolov3.txt

echo "======Test model $model_dir Batch======"
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --gpu_id=0,1 --model_type=det --batch_size=8 1>cpp_results/batch8_yolov3_darknet.txt 2>err
python det/script/diff.py cpp_results/batch8_yolov3_darknet.txt det/py_results/batch8_yolov3_darknet.txt


model_dir="det/models/PPYOLO"
echo "======Test model $model_dir======"
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --model_type=det 1>cpp_results/ppyolo.txt 2>>err
python det/script/diff.py cpp_results/ppyolo.txt det/py_results/ppyolo.txt

model_dir="det/models/FasterRCNN-R50"
echo "======Test model $model_dir======"
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --model_type=det 1>cpp_results/faster.txt 2>>err
python det/script/diff.py cpp_results/faster.txt det/py_results/faster.txt

echo "======Test model $model_dir==Batch===="
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --gpu_id=1 --model_type=det --batch_size=8  1>cpp_results/batch8_fastrcnn.txt 2>>err
python det/script/diff.py cpp_results/batch8_fastrcnn.txt det/py_results/batch8_fastrcnn.txt
model_dir="det/models/FasterRCNN-R50-FPN"

echo "======Test model $model_dir======"
$infer_bin --image_list det/file_list.txt --cfg_file $model_dir/infer_cfg.yml --model_filename $model_dir/__model__ --params_filename $model_dir/__params__ --use_gpu=1 --model_type=det 1>cpp_results/faster_fpn.txt 2>>err
python det/script/diff.py cpp_results/faster_fpn.txt det/py_results/faster_fpn.txt
