// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const that = this
    let sessionId = wx.getStorageSync('SESSIONID')
    let expiredTime = wx.getStorageSync('EXPIREDTIME')
    let now = +new Date()
    if (now  <= expiredTime && sessionId) {
      this.globalData.sessionId = sessionId
      this.globalData.expiredTime = expiredTime
      return
    }
    wx.login({
      success: res => {
        if (res.code) {
          wx.request({
            url: `${getApp().globalData.BASEURL}/wxauth/${res.code}`,
            success: function (res) {
              if (res.statusCode === 200) {
                let session = res.data.session
                that.globalData.sessionId = session
                wx.setStorageSync('SESSIONID', session)
                // 假设登录态保持1天
                let expiredTime = +new Date() + 1 * 24 * 60 * 60 * 1000
                that.globalData.expiredTime = expiredTime
                wx.setStorageSync('EXPIREDTIME', expiredTime)
              }
            }
          })
        } else {
          console.log('获取用户登录态失败！' + res.errMsg)
        }
      },
    })
  },

  globalData: {
    sessionId: null,
    expiredTime: 0,
    BASEURL:'https://www.tzpp.org/tdform',
  }
})