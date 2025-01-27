run_preprocess:
	python -c 'from skin_lens.interface.main import preprocess; preprocess()'

run_train:
	python -c 'from skin_lens.interface.main import train; train()'

run_pred:
	python -c 'from skin_lens.interface.main import pred; pred()'

run_evaluate:
	python -c 'from skin_lens.interface.main import evaluate; evaluate()'
