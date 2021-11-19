// pages/myTempInto/myTempInto.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    formTabTextCol: "black",
    userTabTextCol: "darkseagreen",
    tempintoList: [],
    session: getApp().globalData.sessionId,
    status: ['待处理', '找不到对应联系人', '已生成申请单', '审批中', '通过', '拒绝', '已删除'],
  },
  userTabSelect(e) {},
  formTabSelect(e) {
    wx.redirectTo({
      url: '/pages/tempIntoAdd/tempIntoAdd',
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    var list = wx.getStorageSync("TEMPINTOLIST")
    if (list) { // 本地如果有缓存列表，提前渲染
      that.setData({
        tempintoList: list
      })
    }
    if (!that.data.session) {
      wx.redirectTo({
        url: '/pages/tempIntoAdd/tempIntoAdd',
      })
      return
    }
    wx.request({
      url: 'https://www.tzpp.org/tdform/covidform/tempintos/?weixinid=' + that.data.session,
      success: function (res) {
        if (res.statusCode === 200) {
          let list = res.data
          that.setData({ // 再次渲染列表
            tempintoList: list
          })
          wx.setStorageSync("TEMPINTOLIST", list) // 覆盖缓存数据

        }

      }

    })

  },

  onDelete:function(e){
    console.log(e)
    let id = e.currentTarget.dataset.id
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})