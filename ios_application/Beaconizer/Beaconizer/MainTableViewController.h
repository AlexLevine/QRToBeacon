//
//  MainTableViewController.h
//  
//
//  Created by Alex Levine on 9/6/14.
//
//

#import <UIKit/UIKit.h>

@interface MainTableViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>

    @property (nonatomic, strong) NSArray* UrlsToDisplayInTable;

@end
