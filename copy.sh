for run in workspace/*; do
    [ -d "$run" ] || continue

    run_name=$(basename "$run")

    last_iter=$(find "$run" -maxdepth 1 -type d -name "iteration_*" | sort -V | tail -n 1)

    if [ -n "$last_iter" ]; then
        cp -r "$last_iter" "../POST/${run_name}_final"
    fi
done