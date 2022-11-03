package com.example.appherb

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.appherb.databinding.ActivityMainBinding


class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setUptabbar()

    }
    private fun setUptabbar(){
        binding.menuBottom.setItemSelected(R.id.home)
        val homeFragment = home()
        supportFragmentManager.beginTransaction().replace(R.id.frameLayout,homeFragment).commit()
        binding.menuBottom.setOnItemSelectedListener {
            when(it){
                R.id.home -> {
                    supportFragmentManager.beginTransaction()
                        .replace(R.id.frameLayout,homeFragment)
                        .commit()
                }
                R.id.camera -> {
                    val cameraFragment = camera()
                    supportFragmentManager.beginTransaction()
                        .replace(R.id.frameLayout,cameraFragment)
                        .commit()
                }
                R.id.archive -> {
                    val archiveFragment = archive()
                    supportFragmentManager.beginTransaction()
                        .replace(R.id.frameLayout,archiveFragment)
                        .commit()
                }
                R.id.settings -> {
                    val settingFragment = setting()
                    supportFragmentManager.beginTransaction()
                        .replace(R.id.frameLayout,settingFragment)
                        .commit()
                }

                else -> {

                }
            }
        }
    }
}