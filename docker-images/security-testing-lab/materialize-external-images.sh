#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SNAPSHOTS="${SCRIPT_DIR}/external-image-snapshots.tsv"
if [[ ! -f "$SNAPSHOTS" ]]; then
  printf "Snapshot manifest missing: %s\n" "$SNAPSHOTS" >&2
  exit 1
fi
while IFS=$'\t' read -r local_image build_context upstream_image upstream_digest snapshot_date source_reference; do
  [[ "$local_image" == "local_image" || -z "$local_image" ]] && continue
  printf "Building %s from %s@%s\n" "$local_image" "$upstream_image" "$upstream_digest"
  docker build -t "$local_image" "$SCRIPT_DIR/$build_context"
done < "$SNAPSHOTS"
