# coding:utf-8

from ..const import *

err_msg = {
    ERR_URL_NOT_RECOGNIZED: "網址不夠紳士",
    ERR_CANT_DOWNLOAD_EXH: "需要登錄後才能下載里站",
    ERR_ONLY_VISIBLE_EXH: "這個本子只有里站能看到",
    ERR_MALFORMED_HATHDL: "hathdl文件有貓餅，解析失敗",
    ERR_GALLERY_REMOVED: "這個本子被移除了，大概里站能看到",
    ERR_NO_PAGEURL_FOUND: "沒有找到頁面鏈接，網站改版了嘛？",
    ERR_TASK_NOT_FOUND: "沒有該GUID對應的任務",
    ERR_TASK_LEVEL_UNDEF: "任務過濾等級不存在",
    ERR_DELETE_RUNNING_TASK: "無法刪除運行中的任務",
    ERR_TASK_CANNOT_PAUSE: "這個任務無法被暫停",
    ERR_TASK_CANNOT_RESUME: "這個任務無法被恢復",
    ERR_RPC_PARSE_ERROR: "Parse error.",
    ERR_RPC_INVALID_REQUEST: "Invalid request.",
    ERR_RPC_METHOD_NOT_FOUND: "Method not found.",
    ERR_RPC_INVALID_PARAMS: "Invalid method parameter(s).",
    ERR_RPC_EXEC_ERROR: "",
    ERR_SAVE_SESSION_FAILED: "",
}

ERR_NOMSG = "未指定的錯誤，錯誤號 %d"

XEH_OPT_DESC = "紳♂士下載器"
XEH_OPT_EPILOG = "如果參數未指定，則使用config.py中的默認值"
XEH_OPT_URLS = "下載頁的網址"
XEH_OPT_u = "用戶名"
XEH_OPT_k = "密碼"
XEH_OPT_c = "Cookie字符串，如果指定了用戶名和密碼，此項會被忽略"
XEH_OPT_o = "是否下載原始圖片（如果存在） (當前: %(default)s)"
XEH_OPT_t = "下載線程數 (當前: %(default)d)"
XEH_OPT_f = "快速掃描，從hathdl猜測頁面鏈接，但有時會抽風 (當前: %(default)s)"
XEH_OPT_l = "保存日誌的路徑 (當前: %(default)s)"
XEH_OPT_p = "設置代理, 可以指定多次, 當前支持的類型: socks5/4a, http(s) (當前: %(default)s)"
XEH_OPT_d = "設置下載目錄 (當前: %(default)s)"
XEH_OPT_v = "設置日誌裝逼等級 (當前: %(default)s)"
XEH_OPT_i = "交互模式，如果開啟後台模式，此項會被忽略 (當前: %(default)s)"
XEH_OPT_daemon = "後台模式 (當前: %(default)s)"
XEH_OPT_rpc_port = "設置JSON-RPC監聽IP (當前: %(default)s)"
XEH_OPT_rpc_interface = "設置JSON-RPC監聽埠 (當前: %(default)s)"
XEH_OPT_rpc_secret = "設置JSON-RPC密鑰 (當前: %(default)s)"


PS_LOGIN = "當前沒有登陸，要登陸嗎 (y/n)? > "
PS_USERNAME = "輸入用戶名 > "
PS_PASSWD = "輸入密碼   > "
PS_URL = "輸入地址（使用,分割下載多個）> "
PS_PROXY = "輸入代理地址 (可選) > "
PS_DOWNLOAD_ORI = "是否下載原圖（默認否） (y/n)? > "
PS_DOWNLOAD_DIR = "下載目錄 (當前: %s)\n回車確認或輸入新路徑 > "

PROXY_CANDIDATE_CNT = "代理池中有%d個代理"

TASK_PUT_INTO_WAIT = "任務 #%s 已存在, 加入等待隊列"
TASK_ERROR = "任務 #%s 發生錯誤: %s"
TASK_MIGRATE_EXH = "任務 #%s 使用里站地址重新下載"
TASK_TITLE = "任務 #%s 標題 %s"
TASK_WILL_DOWNLOAD_CNT = "任務 #%s 將下載%d個文件，共%d個 "
TASK_START = "任務 #%s 開始"
TASK_FINISHED = "任務 #%s 完成"
TASK_START_PAGE_RESCAN = "任務 #%s 圖片被縮放，進行完整掃描"
TASK_FAST_SCAN = "任務 #%s 使用快速掃描"

XEH_STARTED = "xeHentai %s 已啟動"
XEH_LOOP_FINISHED = "程序循環已完成"
XEH_LOGIN_EXHENTAI = "登錄紳士"
XEH_LOGIN_OK = "已成為紳士"
XEH_LOGIN_FAILED = "無法登錄紳士"
XEH_LOAD_TASKS_CNT = "從存檔中讀取了%d個任務"
XEH_DAEMON_START = "後台進程已啟動，PID為%d"
XEH_RPC_STARTED = "rpc 伺服器監聽在 %s:%d"
XEH_PLATFORM_NO_DAEMON = "後台模式不支持您的系統: %s"
XEH_CLEANUP = "擦乾淨..."
XEH_CRITICAL_ERROR = "xeHentai 抽風啦:\n%s"

SESSION_LOAD_EXCEPTION = "讀取存檔時遇到錯誤: %s"
SESSION_WRITE_EXCEPTION = "寫入存檔時遇到錯誤: %s"

THREAD = "紳士"
THREAD_UNCAUGHT_EXCEPTION = "紳士-%s 未捕獲的異常\n%s"
THREAD_MAY_BECOME_ZOMBIE = "紳士-%s 可能變成了喪屍"
THREAD_SWEEP_OUT = "紳士-%s 掛了, 不再理它"

QUEUE = "隊列"