# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('frontend', 'frontend'),
    ],
    hiddenimports=[
        # uvicorn internals
        'uvicorn',
        'uvicorn.main',
        'uvicorn.config',
        'uvicorn.server',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.loops.asyncio',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.http.h11_impl',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        # HTTP layer
        'h11',
        'h11._connection',
        'h11._events',
        'h11._util',
        # async IO
        'anyio',
        'anyio._backends._asyncio',
        'anyio.abc',
        'anyio.streams.memory',
        # SQLAlchemy
        'sqlalchemy.dialects.sqlite',
        'sqlalchemy.dialects.sqlite.pysqlite',
        'sqlalchemy.sql.default_comparator',
        # stdlib extras sometimes missed
        'email.mime.text',
        'email.mime.multipart',
        'multiprocessing.spawn',
        'multiprocessing.forkserver',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Krishna Chains',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Krishna Chains',
)

app = BUNDLE(
    coll,
    name='Krishna Chains.app',
    icon=None,
    bundle_identifier='com.krishnachains.billing',
    info_plist={
        'CFBundleDisplayName': 'Krishna Chains',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSPrincipalClass': 'NSApplication',
        'LSMinimumSystemVersion': '10.15.0',
        'NSAppleScriptEnabled': False,
    },
)
