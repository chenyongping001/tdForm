// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    let sessionId = wx.getStorageSync('SESSIONID')
    let expiredTime = wx.getStorageSync('EXPIREDTIME')
    let now = +new Date()
    if (now  <= expiredTime && sessionId) {
      this.globalData.sessionId = sessionId
      this.globalData.expiredTime = expiredTime
    }
  },
  globalData: {
    userInfo: null,
    sessionId: null,
    expiredTime: 0
  }
})