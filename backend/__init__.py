"""minio — provides object storage as the `minio.Storage` DI contract (kernel-redesign extraction).

Binds this plugin's `storage` module (the MinIO/S3 client) into the container under `minio.Storage`, so
the kernel's /api/storage router, lifespan bucket-ensure, and health ping resolve it through the contract
instead of importing a storage module. `minio` pip stays in the kernel image until build-merge lands.
"""
from __future__ import annotations


def register(ctx) -> None:
    from . import storage as storage_impl
    from ...core.contracts import STORAGE

    ctx.container.bind(STORAGE, storage_impl)
