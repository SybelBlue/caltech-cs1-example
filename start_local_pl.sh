mkdir -p "$HOME/pl_ag_jobs" && docker run -it --rm -p 3000:3000 \
    -v "$PWD":/course \
    -v "$HOME/pl_ag_jobs:/jobs" \
    -e HOST_JOBS_DIR="$HOME/pl_ag_jobs" \
    -v /var/run/docker.sock:/var/run/docker.sock \
    prairielearn/prairielearn